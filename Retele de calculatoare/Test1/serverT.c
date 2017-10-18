#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <ctype.h>

void eroare (int check, char* mesaj) {
	if (check < 0) {
		printf("%s\n", mesaj);
		exit(1);
	}
}


pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;
char sir[105];
int len = 0;

int checkSolve(){
	if (strstr(sir,"succes"))
		return 1;
	return 0;
}

void* deservireClient(void* arg) {
	int c = (int)arg;

	char ch;
	recv(c, &ch, sizeof(ch), 0);
	if (!isalpha(ch))
	{
		printf("Nu am primit un caracter.\n");
	}
	else {		
		pthread_mutex_lock(&mtx);

		sir[len++] = ch;
		printf("Sir = %s\n", sir);

		if(checkSolve() == 1)
		{
			printf("Felicitari\n");
			exit(0);
		}

		pthread_mutex_unlock(&mtx);		
	}

	return NULL;
}

int main(int argc, char* argv[]) {
	struct sockaddr_in server, client;
	int s, c, port, l;

	if (argc != 2) eroare(-1, "Use : ./t1s.exe port");

	for (int i = 0; i < strlen(argv[1]); ++i)
		if (!isdigit(argv[1][i]))
		{
			printf("Port incorect.\n" );
			return 0;
		}

	port = atoi(argv[1]);

	s = socket(AF_INET, SOCK_STREAM, 0);
	eroare(s, "Eroare la socket server.");

	memset(&server, 0, sizeof(server));
	memset(&client, 0, sizeof(client));
	l = sizeof(client);

	server.sin_port = htons(port);
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;

	eroare(bind(s, (struct sockaddr *) &server, sizeof(server)), "Eroare la bind server.");

	listen(s, 5);


	while(1) {
		pthread_t thread;

		c = accept(s, (struct sockaddr *) &client, &l);

		eroare(pthread_create(&thread, NULL, deservireClient, (void*)c), "Eroare la crearea threadului.");
	}
	return 0;
}