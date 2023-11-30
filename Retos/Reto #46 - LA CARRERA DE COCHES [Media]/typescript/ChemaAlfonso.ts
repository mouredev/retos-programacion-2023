type Vehicle = { vehicle: string; maxSpeed: number; state: string; timeToRecover?: number }
type Road = string[]
type Path = { participant: Vehicle; road: Road; state: PathState; terrainInCurrentPosition: string }
type Obstacle = { type: string; penalty: number; penaltyEffect: string; min: number; max: number }
type RaceParams = {
	title: string
	distance: number
	participants: Vehicle[]
	obstacles?: Obstacle[]
	raceSpeed?: RaceSpeed
}

enum PathState {
	PENDING = 'pending',
	RUNNING = 'running',
	FINISHED = 'finished'
}

enum RaceState {
	PENDING = 'pending',
	RUNNING = 'running',
	FINISHED = 'finished'
}

export enum RaceSpeed {
	SLOW = 1500,
	NORMAL = 1000,
	FAST = 200
}

export class Race {
	private title: string
	private distance: number
	private raceSpeed: RaceSpeed
	private participants: Vehicle[]
	private obstacles: Obstacle[]
	private raceState: RaceState = RaceState.PENDING
	private time = 0
	private paths: Path[] = []
	private raceResults: { participant: Vehicle; endTime: number }[][] = []
	private awards: string[] = []

	constructor(readonly params: RaceParams) {
		this.title = params.title
		this.distance = params.distance
		this.raceSpeed = params.raceSpeed || RaceSpeed.NORMAL
		this.participants = params.participants
		this.obstacles = params.obstacles || []

		this.prepareAwards()
		this.preparePaths()
	}

	public async start() {
		await this.welcome()
		await this.ready()
		await this.steady()
		await this.go()
	}

	private async welcome() {
		console.clear()
		this.renderTitle()
		await this.wait(2000)
	}

	private async ready() {
		console.clear()
		this.renderTitle()
		console.log('🔴 \x1b[91mReady...\x1b[00m')
		this.renderRace()
		await this.wait(1000)
	}

	private async steady() {
		console.clear()
		this.renderTitle()
		console.log('🟡 \x1b[93mSteady...\x1b[00m')
		this.placeVehiclesOnPaths()
		this.renderRace()
		await this.wait(1000)
	}

	private async go() {
		console.clear()
		this.renderTitle()
		console.log('🟢 \x1b[92mGo!!!\x1b[00m')
		this.runTimer()
		this.renderRace()
		await this.wait(1000)

		this.raceState = RaceState.RUNNING
		this.paths.forEach(path => (path.state = PathState.RUNNING))

		while (this.raceState === RaceState.RUNNING) {
			console.clear()
			this.renderTitle()
			this.renderTime()
			this.moveVehicles()
			this.renderRace()
			this.setFinishedParticipants()

			if (this.paths.every(path => path.state === PathState.FINISHED)) {
				this.raceState = RaceState.FINISHED
			} else {
				await this.wait(this.raceSpeed)
			}
		}

		this.giveAwards()
	}

	// Race state renderers
	private renderTitle() {
		console.log(`----------- 🏁 \x1b[94m${this.title} GP \x1b[00m🏁 -----------\n`)
	}

	private renderRace() {
		console.log(`\n${this.paths.map(path => path.road.join('')).join('\n')}`)
	}

	private renderTime() {
		console.log(`Elapsed time: ${this.time} seconds`)
	}

	private giveAwards() {
		console.clear()
		this.renderTitle()
		console.log(`\x1b[92m------- Race results -------\x1b[00m\n`)

		const results = this.raceResults
			.map((endResults, idx) => {
				const endTime = endResults[0].endTime
				return `[${this.awards[idx]}] [${endTime}s] => ${endResults
					.map(endResult => endResult.participant.vehicle)
					.join(' | ')}`
			})
			.join('\n')

		console.log(results)
	}

	private setFinishedParticipants() {
		const endPosition = this.raceResults.length

		this.paths.forEach(path => {
			const { road, participant, state } = path

			if (state === PathState.FINISHED || road[0] !== participant.vehicle) return

			path.state = PathState.FINISHED

			if (!this.raceResults[endPosition]) this.raceResults[endPosition] = []

			this.raceResults[endPosition].push({ participant, endTime: this.time })
		})
	}

	// Race actions
	private placeVehiclesOnPaths(): void {
		this.paths.forEach(path => {
			path.road[path.road.length - 1] = path.participant.vehicle
		})
	}

	private moveVehicles() {
		this.paths.forEach(path => {
			if (path.state === PathState.FINISHED) return

			if (path.participant.timeToRecover) {
				path.participant.timeToRecover--
				return
			}

			const movement = Math.floor(Math.random() * path.participant.maxSpeed) + 1
			const currentPosition = path.road.indexOf(path.participant.state)
			const finalPosition = Math.max(currentPosition - movement, 0)
			const terrainTypeInFinalPosition = path.road[finalPosition]
			const obstacleInFinalPosition = this.getObstacleByType(terrainTypeInFinalPosition)

			if (obstacleInFinalPosition) {
				path.participant.state = obstacleInFinalPosition.penaltyEffect
				path.participant.timeToRecover = obstacleInFinalPosition.penalty
			} else {
				path.participant.state = path.participant.vehicle
			}

			// Reset terrain on leaving position
			path.road.splice(currentPosition, 1, path.terrainInCurrentPosition)

			// Replace terrain in final position with participant vehicle
			path.road.splice(finalPosition, 1, path.participant.state)

			path.terrainInCurrentPosition = terrainTypeInFinalPosition
		})
	}

	private async runTimer() {
		await this.wait(this.raceSpeed)
		this.time++

		if (this.raceState === RaceState.FINISHED) return

		await this.runTimer()
	}

	// Race preparation
	private prepareAwards() {
		this.awards = ['🥇', '🥈', '🥉']

		for (let i = 0; i < this.participants.length - 3; i++) {
			this.awards.push('🏅')
		}
	}

	private preparePaths() {
		this.participants.forEach(participant => {
			this.paths.push({
				participant: participant,
				road: this.buildRoad(),
				state: PathState.PENDING,
				terrainInCurrentPosition: '_'
			})
		})
	}

	private buildRoad(): Road {
		const roadUnderConstruction: string[] = []

		const obstaclesToAdd: string[] = this.obstacles.flatMap(({ type, min, max }) => {
			const obstaclesToAddOfCurrentType = Math.floor(Math.random() * (max - min + 1)) + min
			return Array(obstaclesToAddOfCurrentType).fill(type)
		})
		const plainTerrain: string[] = Array(this.distance - obstaclesToAdd.length - 2).fill('_')

		roadUnderConstruction.push(...obstaclesToAdd, ...plainTerrain)

		const road = roadUnderConstruction.toSorted((a, b) => (Math.random() > 0.5 ? 1 : -1))

		road.unshift('🏁')
		road.push('_')

		return road
	}

	// Helpers
	private getObstacleByType(terrain: string): Obstacle | undefined {
		return this.obstacles.find(obstacle => obstacle.type === terrain)
	}

	async wait(ms: number) {
		return new Promise(resolve => setTimeout(resolve, ms))
	}
}

// ===================================
// Reto GP
// ===================================
const raceParams: RaceParams = {
	title: 'Moure Reto #46',
	distance: 20,
	raceSpeed: RaceSpeed.NORMAL,
	participants: [
		{ vehicle: '🚙', state: '🚙', maxSpeed: 3 },
		{ vehicle: '🚗', state: '🚗', maxSpeed: 3 }
	],
	obstacles: [{ type: '🌲', penalty: 1, penaltyEffect: '💥', min: 1, max: 3 }]
}
const race = new Race(raceParams)
race.start()

// ===================================
// Random GPs
// ===================================
// ;(async () => {
// 	const randomRaceCreator = (minDistance: number, maxDistance: number, raceSpeed: RaceSpeed): RaceParams => {
// 		const contexts = [
// 			{
// 				name: 'Urban',
// 				vehicleType: ['🚙', '🚗', '🚕', '🚚', '🚓', '🏎️'],
// 				obstacles: [
// 					{ type: '🚦', penalty: 1, penaltyEffect: '🛑', min: 1, max: 3 },
// 					{ type: '🚧', penalty: 2, penaltyEffect: '💥', min: 1, max: 3 }
// 				]
// 			},
// 			{
// 				name: 'Desert',
// 				vehicleType: ['🚙', '🚗', '🚕', '🚚'],
// 				obstacles: [
// 					{ type: '🌵', penalty: 2, penaltyEffect: '🔥', min: 1, max: 2 },
// 					{ type: '🌴', penalty: 1, penaltyEffect: '💥', min: 1, max: 2 },
// 					{ type: '🏜️', penalty: 3, penaltyEffect: '🔥', min: 1, max: 2 }
// 				]
// 			},
// 			{
// 				name: 'Mountain',
// 				vehicleType: ['🚴', '🏍️', '🚜'],
// 				obstacles: [
// 					{ type: '🌲', penalty: 1, penaltyEffect: '💥', min: 1, max: 2 },
// 					{ type: '🌳', penalty: 3, penaltyEffect: '💥', min: 1, max: 2 },
// 					{ type: '🪨', penalty: 3, penaltyEffect: '💥', min: 1, max: 2 }
// 				]
// 			},
// 			{
// 				name: 'Aquatic',
// 				vehicleType: ['🚤', '🛶', '🚣', '🏄', '🛥️'],
// 				obstacles: [
// 					{ type: '🐟', penalty: 1, penaltyEffect: '🌊', min: 1, max: 2 },
// 					{ type: '🦀', penalty: 2, penaltyEffect: '🌊', min: 1, max: 2 },
// 					{ type: '🦈', penalty: 3, penaltyEffect: '🌊', min: 1, max: 2 }
// 				]
// 			}
// 		]

// 		const randomContext = contexts[Math.floor(Math.random() * contexts.length)]

// 		return {
// 			title: randomContext.name,
// 			distance: Math.floor(Math.random() * (maxDistance - minDistance + 1)) + minDistance,
// 			participants: randomContext.vehicleType.map(vehicle => ({
// 				vehicle,
// 				state: vehicle,
// 				maxSpeed: Math.floor(Math.random() * 5) + 1
// 			})),
// 			obstacles: randomContext.obstacles,
// 			raceSpeed: raceSpeed
// 		}
// 	}

// 	let count = 1
// 	while (true) {
// 		console.clear()
// 		console.log(`Round ${count++}`)
// 		await new Promise(resolve => setTimeout(resolve, 1000))
// 		await new Race(randomRaceCreator(30, 40, RaceSpeed.FAST)).start()
// 		await new Promise(resolve => setTimeout(resolve, 3000))
// 	}
// })()
