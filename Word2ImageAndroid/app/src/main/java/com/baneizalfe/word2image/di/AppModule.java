package com.baneizalfe.word2image.di;

import android.app.Application;
import android.content.Context;

import javax.inject.Singleton;

import dagger.Module;
import dagger.Provides;

/**
 * Created by baneizalfe on 26.12.17.
 */

@Module(includes = {ViewModelModule.class})
public class AppModule {

    private Application mApplication;

    public AppModule(Application application) {
        mApplication = application;
    }

    @Provides
    @Singleton
    public Application provideApplication() {
        return mApplication;
    }

    @Provides
    @Singleton
    public Context provideContext() {
        return mApplication.getBaseContext();
    }
}
