package com.baneizalfe.word2image.di;

import android.arch.lifecycle.ViewModel;
import android.arch.lifecycle.ViewModelProvider;

import com.baneizalfe.word2image.ui.MyViewModelFactory;
import com.baneizalfe.word2image.ui.main.MainAVM;

import dagger.Binds;
import dagger.Module;
import dagger.multibindings.IntoMap;

/**
 * Created by baneizalfe on 26.12.17.
 */

@Module
public abstract class ViewModelModule {

    @Binds
    @IntoMap
    @ViewModelKey(MainAVM.class)
    abstract ViewModel bindsMainAVM(MainAVM mainAVM);

    @Binds
    abstract ViewModelProvider.Factory bindsViewModelFactory(MyViewModelFactory MyViewModelFactory);
}
