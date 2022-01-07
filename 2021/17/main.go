package main

import "fmt"

// target area: x=241..273, y=-97..-63

type Probe struct {
	x  int
	y  int
	sx int
	sy int
}

func (p *Probe) Step() {
	p.x = p.x + p.sx
	p.y = p.y + p.sy
	if p.sx > 0 {
		p.sx -= 1
	} else if p.sx < 0 {
		p.sx += 1
	}
	p.sy -= 1
}

func (p Probe) InZone() bool {
	return 241 <= p.x && p.x <= 273 && -97 <= p.y && p.y <= -63
}

func (p Probe) Out() bool {
	return p.y < -97
}

func NewProbe(sx, sy int) *Probe {
	return &Probe{x: 0, y: 0, sx: sx, sy: sy}
}

func main() {
	ymax := 0
	cnt := 0
	for sx := 0; sx <= 273; sx++ {
		for sy := -97; sy <= 2730; sy++ {
			p := NewProbe(sx, sy)
			inzone := false
			yloc := p.y
			for p.Out() == false {
				p.Step()
				if p.y > yloc {
					yloc = p.y
				}
				if inzone == false {
					inzone = p.InZone()
				}
			}
			if inzone == true {
				if yloc > ymax {
					ymax = yloc
				}
				cnt += 1
			}
		}
	}
	fmt.Printf("%v %v\n", ymax, cnt)
}
