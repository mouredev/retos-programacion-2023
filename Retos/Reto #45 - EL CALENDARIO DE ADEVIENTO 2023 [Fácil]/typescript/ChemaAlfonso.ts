import { createInterface } from 'node:readline'
import { stdin as input, stdout as output } from 'node:process'

type UserCommunicator = {
	makeQuestion: (questionToMake: string) => Promise<string>
	tellSomething: (somethingToTell: string) => void
	forgetTold: () => void
	endCommunication: () => void
}

export class AdevientoCalendar {
	private participants: string[] = []
	private running = true
	private output = ''
	private outputColor = ''
	private colors = {
		ok: '\x1b[92m',
		ko: '\x1b[91m'
	}

	constructor(private readonly userCommunicator: UserCommunicator) {}

	async run() {
		const menu = Object.values(this.getMenuOptions())
			.map((option, idx) => `${idx + 1}. ${option.optionName}`)
			.join('\n')

		while (this.running) {
			// Select action
			this.userCommunicator.forgetTold()
			this.userCommunicator.tellSomething(this.title())
			this.userCommunicator.tellSomething(menu)

			if (this.output) this.userCommunicator.tellSomething(`\n${this.outputColor}${this.output}\x1b[00m`)

			const selectedOption = await this.userCommunicator.makeQuestion('\n\x1b[93m¿Qué quieres hacer?\x1b[00m')

			// Handle selected action
			this.userCommunicator.forgetTold()
			this.outputColor = this.colors.ok
			this.userCommunicator.tellSomething(this.title())

			const handler = this.getMenuOptions()[+selectedOption - 1]?.handler
			if (!handler) {
				this.outputColor = this.colors.ko
				this.output = 'Selecciona una opción válida...'
				continue
			}

			await handler()
		}
	}

	private async addParticipant() {
		const name = await this.userCommunicator.makeQuestion('Dime el nombre del participante:')

		if (this.participantAlreadyExists(name)) {
			this.outputColor = this.colors.ko
			this.output = 'El participante ya existe'
			return
		}

		this.participants.push(name)
		this.output = `Se ha añadido a '${name}' a los participantes`
	}

	private async removeParticipant() {
		const removingName = await this.userCommunicator.makeQuestion('Dime el nombre del participante:')

		if (!this.participantAlreadyExists(removingName)) {
			this.outputColor = this.colors.ko
			this.output = 'El participante no existe'
			return
		}

		this.participants = this.participants.filter(name => name !== removingName)
		this.output = `Se ha eliminado a '${removingName}' de los participantes`
	}

	private listParticipants() {
		if (!this.participants.length) {
			this.outputColor = this.colors.ko
			this.output = 'No hay ningún participante'
			return
		}

		const participantsList = this.participants.map(option => `- ${option}`).join('\n')
		const total = `${this.participants.length} participantes en total.`
		this.output = `${participantsList}\n\n${total}`
	}

	private sortout() {
		if (!this.participants.length) {
			this.outputColor = this.colors.ko
			this.output = 'No hay ningún participante'
			return
		}

		const winnerIdx = Math.floor(Math.random() * this.participants.length)
		const winner = this.participants[winnerIdx]
		this.output = `El ganador es '${winner}'! 🥳 🎊 🎉`

		this.participants.splice(winnerIdx, 1)
	}

	private exit() {
		this.userCommunicator.tellSomething('Hasta otra 👋!')
		this.userCommunicator.endCommunication()
		this.running = false
	}

	private participantAlreadyExists(name: string) {
		return this.participants.includes(name)
	}

	private title() {
		return `\x1b[95m
			███████	██████  ███████ ██    ██ ██ ███████ ███    ██ ████████  ██████  
			██   ██ ██   ██ ██      ██    ██ ██ ██      ████   ██    ██    ██    ██ 
			███████ ██   ██ █████   ██    ██ ██ █████   ██ ██  ██    ██    ██    ██ 
			██   ██ ██   ██ ██       ██  ██  ██ ██      ██  ██ ██    ██    ██    ██ 
			██   ██ ██████  ███████   ████   ██ ███████ ██   ████    ██     ██████  Calendar.
		\x1b[00m`
	}

	private getMenuOptions() {
		return [
			{
				optionName: 'Añadir participante',
				handler: this.addParticipant.bind(this)
			},
			{
				optionName: 'Eliminar participante',
				handler: this.removeParticipant.bind(this)
			},
			{
				optionName: 'Listar participantes',
				handler: this.listParticipants.bind(this)
			},
			{
				optionName: 'Sortear',
				handler: this.sortout.bind(this)
			},
			{
				optionName: 'Salir',
				handler: this.exit.bind(this)
			}
		]
	}
}

// Create communicator
const inputInterface = createInterface({ input, output })
const communicator: UserCommunicator = {
	makeQuestion: (questionToMake: string): Promise<string> => {
		return new Promise(resolve => {
			inputInterface.question(`${questionToMake}\n`, (answer: string) => {
				resolve(answer)
			})
		})
	},
	tellSomething: somethingToTell => console.log(somethingToTell),
	forgetTold: () => console.clear(),
	endCommunication: inputInterface.close.bind(inputInterface)
}

// Start
new AdevientoCalendar(communicator).run()
