package com.github;

public class Main {
    public static void main(String[] args) {
        int kronMatrixDepth = Integer.valueOf(args[0]);
        System.out.println("kronecker matrix depth="+kronMatrixDepth + " regular matrix depth will be ^2");


        JavaBenchmark bench = new JavaBenchmark(kronMatrixDepth);
        // warming up JVM if specified
        int warmUpCycles = 0;
        try {
            warmUpCycles = Integer.valueOf(args[1]);
        } catch (java.lang.ArrayIndexOutOfBoundsException e) {}

        bench.warmUp(warmUpCycles);


        System.out.println("Stating EJML benchmark...");
//        Timer.measureTime(bench::ejmlMult);
        Timer.measureTime(bench::ejmlKron);
        Timer.measureTime(bench::ejmlHadamard);
    }
}