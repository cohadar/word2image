package com.baneizalfe.word2image.di;

import com.baneizalfe.word2image.ui.main.MainActivity;
import com.baneizalfe.word2image.ui.main.MainBuilderModule;

import dagger.Module;
import dagger.android.ContributesAndroidInjector;

/**
 * Created by baneizalfe on 26.12.17.
 */

@Module
public abstract class ActivityBuilderModule {

    @ContributesAndroidInjector(modules = {MainBuilderModule.class})
    abstract MainActivity mainActivity();
}
