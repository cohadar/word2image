package com.baneizalfe.word2image.di;

import com.baneizalfe.word2image.App;

import javax.inject.Singleton;

import dagger.Component;
import dagger.android.AndroidInjectionModule;

/**
 * Created by baneizalfe on 26.12.17.
 */

@Singleton
@Component(modules = {
        AndroidInjectionModule.class,
        AppModule.class,
        NetworkModule.class,
        ManagerModule.class,
        ActivityBuilderModule.class
})
public interface AppComponent {

    @Component.Builder
    interface Builder {

        Builder appModule(AppModule appModule);

        Builder networkModule(NetworkModule networkModule);

        AppComponent build();
    }

    void inject(App app);
}