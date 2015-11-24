// by cmotevasselani

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<fcntl.h>
#include<unistd.h>
#include<errno.h>

#ifndef __CAM_LOG__
#define __CAM_LOG__
char * LOG_EXT = ".log";

enum LogLevel {
  INFO = 0,
  WARN,
  DEBUG
};

struct Logger {
  char * name;
  char ** msgs;
  int numMsgs;
  int logFd;
  enum LogLevel logLevel;
};

void logMsg(struct Logger *, int, char *);

struct Logger * createLogger(char *, enum LogLevel);

#endif
