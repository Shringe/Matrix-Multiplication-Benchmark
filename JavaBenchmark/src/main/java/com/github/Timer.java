package com.github;

public class Timer {
    public static void measureTime(Runnable method) {
        long startTime = System.nanoTime();
        method.run();
        long endTime = System.nanoTime();
        long executionTime = endTime - startTime;

        double executionTimeMillis = (double) executionTime/1000000;

        System.out.println("::" + executionTimeMillis);
    }
}
