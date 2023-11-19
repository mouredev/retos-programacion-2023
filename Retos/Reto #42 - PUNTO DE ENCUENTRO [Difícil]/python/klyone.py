#!/usr/bin/env python3

class World:
    def __init__(self, max_x, max_y, max_time):
        self.max_x = max_x
        self.max_y = max_y
        self.max_time = max_time
        self.particles = []
        self.meeting_point = None

    def reset(self):
        self.particles = []
        self.meeting_point = None

    def attach_particle(self, p):
        self.particles.append(p)

    def check_particles_pos_limits(self):
        ok = True
        for p in self.particles:
            pos = p.get_pos()

            if pos[0] > self.max_x or pos[1] > self.max_y:
                ok = False
                break
        return ok

    def check_particles_meeting_point(self):
        found = True

        point = self.particles[0].get_pos()

        for p in self.particles:
            if point != p.get_pos():
                found = False
                break

        return found

    def update_particles(self):
        for p in self.particles:
            p.update()

    def run(self):
        self.meeting_points = None

        if len(self.particles) <= 1:
            return

        if not self.check_particles_pos_limits():
            return

        if self.check_particles_meeting_point():
            self.meeting_point = [0, self.particles[0].get_pos()]
            return

        for t in range(1, self.max_time):
            self.update_particles()

            if not self.check_particles_pos_limits():
                break

            if self.check_particles_meeting_point():
                self.meeting_point = [t, self.particles[0].get_pos()]
                break

    def get_meeting_point(self):
        return self.meeting_point

class Particle:
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed
    def update_pos(self, t):
        self.pos[0] += self.speed[0] * t
        self.pos[1] += self.speed[1] * t
    def update(self):
        self.update_pos(1)
    def get_pos(self):
        return self.pos

if __name__ == "__main__":
    p1 = Particle([0,0], [1,1])
    p2 = Particle([0,10], [1,0])
    w = World(100,100,100)
    w.attach_particle(p1)
    w.attach_particle(p2)
    w.run()
    print(w.get_meeting_point())

    p1 = Particle([0,0], [1,2])
    p2 = Particle([0,0], [-1,-1])
    w.reset()
    w.attach_particle(p1)
    w.attach_particle(p2)
    w.run()
    print(w.get_meeting_point())

    p1 = Particle([0,0], [1,2])
    p2 = Particle([10,0], [10,22])
    w.reset()
    w.attach_particle(p1)
    w.attach_particle(p2)
    w.run()
    print(w.get_meeting_point())
