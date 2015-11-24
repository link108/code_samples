#include "logger.c"

int main() {
  struct Logger * logger = createLogger("simpleLogger", INFO);
  if (NULL != logger) {
    logMsg(logger, WARN, "msg");
    logMsg(logger, INFO, "msg1");
    logMsg(logger, DEBUG, "msg2");
  }
  close(logger->logFd);
  free(logger);
  return 0;
}

