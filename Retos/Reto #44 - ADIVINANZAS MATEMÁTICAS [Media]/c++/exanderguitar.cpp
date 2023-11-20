#include <iostream>
#include <chrono>
#include <random>
#include <cmath>

enum MathOperator {
		ADD,
		SUBSTRACT,
		MULTIPLY,
		DIVIDE
};

void getTime (std::chrono::steady_clock::time_point& timePoint); 
double calculateInterval (std::chrono::steady_clock::time_point start, std::chrono::steady_clock::time_point end); 
bool game (int& level, int& prevLevel, double timeLimit, int& digitLeft, int& digitRight);
int prepareQuestion (int rightAnswers, int prevLevel, int& digitLeft, int& digitRight); 
int randomNumber (int digits); 
void randomOperator (MathOperator& quizOperator);

int main() {

	bool finish {false};
	int currentLevel {1};
	int previousLevel {1};
	double timeLimit {20.0};
	int leftDigit {1};
	int rightDigit {1};

	while(!finish) {
		finish = game(currentLevel, previousLevel, timeLimit, leftDigit, rightDigit);
	}

	std::cout << '\n';
	std::cout << "Has tenido " << currentLevel - 1<< " aciertos.\n";

	return 0;
}

void getTime (std::chrono::steady_clock::time_point& timePoint) {

	timePoint = std::chrono::steady_clock::now();

}

double calculateInterval (std::chrono::steady_clock::time_point start, std::chrono::steady_clock::time_point end) {

	std::chrono::duration<double> timeInterval = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);

	return timeInterval.count();
}

bool game(int& level, int& prevLevel,  double timeLimit, int& digitLeft, int& digitRight) {

	std::chrono::steady_clock::time_point startTime {};
	std::chrono::steady_clock::time_point endTime {};

	std::cout << "¡Ponte a prueba con adivinanzas matematicas!\n\n";
	std::cout << "Nivel " << level << "\n\n";

	int result {prepareQuestion (level, prevLevel, digitLeft, digitRight)};	

	getTime (startTime);

	int userAnswer {};
	std::cin >> userAnswer;

	std::cout << '\n';

	getTime (endTime);
	double interval {calculateInterval (startTime, endTime)};

	if(result == userAnswer) {
		std::cout << "¡Correcto!\n";
		level++;
	}
	else {
		std::cout << "¡Incorrecto! El resultado era: " << result << '\n';
		prevLevel = level;
	}

	if(interval > timeLimit) {
		std::cout << "Lo siento, pero has tardado demasiado en responder.\n";
		return true;
	}

	return false;
}	

int prepareQuestion (int rightAnswers, int prevLevel, int& digitLeft, int& digitRight) {

	MathOperator quizOperator {};
	randomOperator (quizOperator);

	if(rightAnswers % 5 == 0 && prevLevel != rightAnswers) {
		if(digitLeft == digitRight) {
			digitLeft++;
		}
		else {
			digitRight++;
		}
	}
		
	int leftOperand {randomNumber(digitLeft)};
	int rightOperand {randomNumber(digitRight)};
	int result {};

	switch(quizOperator) {
	case ADD:
		std::cout << leftOperand << " + " << rightOperand << " = ";
		result = leftOperand + rightOperand;
		break;
	case SUBSTRACT:
		std::cout << leftOperand << " - " << rightOperand << " = ";
		result = leftOperand - rightOperand;
		break;
	case MULTIPLY:
		std::cout << leftOperand << " * " << rightOperand << " = ";
		result = leftOperand * rightOperand;
		break;
	case DIVIDE:
		if(rightOperand == 0) {
			rightOperand++;
		}
		std::cout << leftOperand << " / " << rightOperand << " = ";
		result = leftOperand / rightOperand;
		break;
	default:
		std::cout << "Error in prepareQuestion switch\n";
		break;
	}

	return result;
}

int randomNumber (int digits) {

	int upperLimit {static_cast<int>(std::pow(10, digits) - 1)};	

	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<int> numberDis(0, upperLimit);

	return numberDis(gen);
}

void randomOperator (MathOperator& quizOperator) {

	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<int> numberDis(0,3);

	switch(numberDis(gen)) {
	case 0:
		quizOperator = ADD;
		break;
	case 1:
		quizOperator = SUBSTRACT;
		break;
	case 2:
		quizOperator = MULTIPLY;
		break;
	case 3:
		quizOperator = DIVIDE;
		break;
	default:
		std::cout << "Error in switch operator\n";
	}	
}
