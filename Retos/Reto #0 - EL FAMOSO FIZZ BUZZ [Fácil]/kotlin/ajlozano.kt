package edu.tlozano.weeklychallenge2023

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

private const val FIZZ = "fizz"
private const val BUZZ = "buzz"
private const val THREE = 3
private const val FIVE = 5

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        fizzbuzz()
    }

    private fun fizzbuzz() {
        for (i in 1..100) {
            if (i % THREE != 0 && i % FIVE != 0)
                print(i)
            if (i % THREE == 0)
                print(FIZZ)
            if (i % FIVE == 0)
                print(BUZZ)
            println("")
        }
    }
}
