CREATE TABLE Timer(
    id Serial PRIMARY KEY,
    title Text,
    startTime time,
    endTime time,
    totalTime time
);