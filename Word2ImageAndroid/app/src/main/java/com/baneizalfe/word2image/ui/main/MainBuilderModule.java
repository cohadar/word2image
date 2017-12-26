package com.baneizalfe.word2image.ui.main;

import com.baneizalfe.word2image.ui.main.form.FormFragment;
import com.baneizalfe.word2image.ui.main.results.ResultsFragment;

import dagger.Module;
import dagger.android.ContributesAndroidInjector;

/**
 * Created by baneizalfe on 26.12.17.
 */

@Module
public abstract class MainBuilderModule {

    @ContributesAndroidInjector
    abstract FormFragment contributeFormFragment();

    @ContributesAndroidInjector
    abstract ResultsFragment contributeResultsFragment();
}