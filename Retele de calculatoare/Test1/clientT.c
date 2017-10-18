#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <ctype.h>


void executa (int c) {

	char ch;
	printf("Introduceti un caracter\n");
	scanf("%c", &ch);
	send(c, &ch, sizeof(ch), 0);
}

void eroare(int check, char* mesaj) {
	if (check < 0) {
		printf("%s\n", mesaj);
		exit(1);
	}
}

int main(int argc, char* argv[]) {
	struct sockaddr_in server;
	int c, port;
	char* ip;

	if (argc != 3) {
		eroare(-1, "Use : ./t1c.exe port ip");
	}

	for (int i = 0; i < strlen(argv[1]); ++i)
		if (!isdigit(argv[1][i]))
		{
			printf("Port incorect.\n" );
			return 0;
		}

	port = atoi(argv[1]);
	if (port < 1024 || port > 9999) //1024-9999
	ip = argv[2];

	c = socket(AF_INET, SOCK_STREAM, 0);

	memset(&server, 0, sizeof(server));
	server.sin_family = AF_INET;
	server.sin_port = htons(port);
	server.sin_addr.s_addr = inet_addr(ip);

	eroare(connect(c, (struct sockaddr *) &server, sizeof(server)), "Eroare la conectarea la server.");

	executa(c);

	return 0;
}