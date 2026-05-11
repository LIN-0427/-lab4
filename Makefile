CC = gcc
TARGET = program
SRC = main.c utils.c
HDR = utils.h

all: $(TARGET)

$(TARGET): $(SRC) $(HDR)
	$(CC) $(SRC) -o $(TARGET)

clean:
	rm -f $(TARGET)

run: $(TARGET)
	./$(TARGET)
