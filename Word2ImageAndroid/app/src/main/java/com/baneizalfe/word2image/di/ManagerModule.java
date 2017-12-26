package com.baneizalfe.word2image.di;

import com.baneizalfe.word2image.core.managers.WordManager;
import com.baneizalfe.word2image.core.network.services.WordService;

import javax.inject.Singleton;

import dagger.Module;
import dagger.Provides;

/**
 * Created by baneizalfe on 26.12.17.
 */

@Module
public class ManagerModule {

    @Provides
    @Singleton
    WordManager provideStorageManager(WordService wordService) {
        return new WordManager(wordService);
    }
}
