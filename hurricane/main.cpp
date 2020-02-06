#include <iostream>

int main() {
	std::cout << "Hallo Welt\n";
	int a[5] = { 1,24,4,2,12 };
	for (int i : a) {
		std::cout << i;
	}
	std::cin.get();
}