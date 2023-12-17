package com.github;

import org.ejml.simple.SimpleMatrix;

import java.util.Random;

public class JavaBenchmark {
    public final Random random = new Random();

    // regular matrices
    public final SimpleMatrix m1;
    public final SimpleMatrix m2;

    public final SimpleMatrix columnVector = new SimpleMatrix(10000, 10000);


    // kron matrices
    public final SimpleMatrix m1k;
    public final SimpleMatrix m2k;

    public JavaBenchmark(int kronMatrixDepth) {
        // squaring to find equivalent matrix depth
        int matrixDepth = (int) Math.pow(kronMatrixDepth, 2);

        System.out.println("Creating matrices");
        this.m1 = SimpleMatrix.random(matrixDepth, matrixDepth);
        this.m2 = SimpleMatrix.random(matrixDepth, matrixDepth);
        this.m1k = SimpleMatrix.random(kronMatrixDepth, kronMatrixDepth);
        this.m2k = SimpleMatrix.random(kronMatrixDepth, kronMatrixDepth);

        this.columnVector.fill(0.0);
    }

    public void warmUp(int numOfTimes) {
        // warm up JVM
        System.out.println("Going through " +numOfTimes+ " warm up cycles...");
        for (int i = 0; i < numOfTimes; i++) {
//            ejmlMult();
            ejmlKron();
            ejmlHadamard();
            System.out.println("Warm up cycle " + (i+1) + " complete.");
        }
    }

    public SimpleMatrix ejmlMult() {
        return m1.mult(m2);
    }

    public SimpleMatrix ejmlKron() {
        return m1k.kron(m2k);
    }

    public SimpleMatrix ejmlHadamard() {
        return m1.elementMult(m2);
    }

}