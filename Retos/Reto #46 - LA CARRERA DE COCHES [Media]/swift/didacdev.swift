import Foundation


class Track {

    private var track: [Item] = []
    private var trackLength: Int
    private var car: String = ""
    private var finish: Bool = false
    private var crash: Bool = false

    private enum Item {
        case tree
        case road
        case goal
        case car
        case crash
    }

    init(trackLength: Int, car: String) {

        self.trackLength = trackLength
        self.car = car
        self.track = setTrack(treesPositions: setTrees())
    }

    private func setTrees() -> [Int]{
        let numberOfTrees = Int.random(in: 1...3)
        var treesPositions = [Int]()

        for _ in 1...numberOfTrees {

            let position = Int.random(in: 1..<trackLength)
            treesPositions.append(position)

        }

        return treesPositions
    }

    private func setTrack(treesPositions: [Int]) -> [Item]{

        var track = [Item]()

        track.append(Item.goal)

        for position in 1..<trackLength {

            if treesPositions.contains(position) {
                track.append(Item.tree)
            } else {
                track.append(Item.road)
            }
        }

        track.append(Item.car)
        return track

    }

    func printTrack() {

        var stringTrack = ""

        for position in track {

            switch position {
            case Item.goal:
                stringTrack.append("🏁")
            case Item.tree:
                stringTrack.append("🌲")
            case Item.road:
                stringTrack.append("_")
            case Item.car:
                stringTrack.append(car)
            case Item.crash:
                stringTrack.append("💥")
            }
        }

        print(stringTrack)
    }

    func moveCar(positions: Int) {

        if !crash {

            track.popLast() //Remove car

            if positions > 1 {

                for _ in 1..<positions {

                    if track.count > 1 {

                        track.popLast()

                    } else {

                        finish = true
                        break
                    }
                }
            }

            if !finish {

                if let item = track.last {

                    if item == Item.tree {

                        crash = true
                        track.popLast()
                        track.append(Item.crash)

                    } else if item == Item.goal {

                        finish = true
                        track.popLast()
                        track.append(Item.crash)

                    } else {

                        track.popLast()
                        track.append(Item.car)

                    }
                }
            }

        } else {

            crash = false

        }

    }

    func isFinish() -> Bool {
        return finish
    }

    func isCrash() -> Bool {
        return crash
    }

}

class Race {
    private var trackOne: Track
    private var trackTwo: Track

    init(trackLength: Int) {
        self.trackOne = Track(trackLength: trackLength, car: "🚙")
        self.trackTwo = Track(trackLength: trackLength, car: "🚗")
    }

    func printTracks() {
        trackOne.printTrack()
        trackTwo.printTrack()
    }

    func moveCars() {
        trackOne.moveCar(positions: Int.random(in: 1...3))
        trackTwo.moveCar(positions: Int.random(in: 1...3))
    }

    func getTrackOne() -> Track {
        return trackOne
    }

    func getTrackTwo() -> Track {
        return trackTwo
    }
}

func startRace(trackLength: Int) {

    let race = Race(trackLength: trackLength)

    repeat {
        print()
        race.printTracks()
        race.moveCars()
        sleep(1)
    } while !race.getTrackOne().isFinish() && !race.getTrackTwo().isFinish()

    print()
    if race.getTrackOne().isFinish() {
        print("Gana 🚙!")
    } else if race.getTrackTwo().isFinish() {
        print("Gana 🚗!")
    }

}

startRace(trackLength: 40)




