package com.baneizalfe.word2image.ui.main;

import android.arch.lifecycle.ViewModelProvider;
import android.arch.lifecycle.ViewModelProviders;
import android.support.v4.app.Fragment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.baneizalfe.word2image.R;
import com.baneizalfe.word2image.ui.main.form.FormFragment;
import com.baneizalfe.word2image.ui.main.results.ResultsFragment;

import javax.inject.Inject;

import dagger.android.AndroidInjector;
import dagger.android.DispatchingAndroidInjector;
import dagger.android.support.HasSupportFragmentInjector;

public class MainActivity extends AppCompatActivity implements HasSupportFragmentInjector {

    @Inject
    DispatchingAndroidInjector<Fragment> dispatchingAndroidInjector;

    @Inject
    ViewModelProvider.Factory viewModelFactory;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if (savedInstanceState == null) {
            showFormScreen();
        }
    }

    @Override
    public AndroidInjector<Fragment> supportFragmentInjector() {
        return dispatchingAndroidInjector;
    }

    void showFormScreen() {
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.main_content, new FormFragment())
                .commitAllowingStateLoss();
    }

    void showResultsScreen() {
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.main_content, new ResultsFragment())
                .commitAllowingStateLoss();
    }
}
