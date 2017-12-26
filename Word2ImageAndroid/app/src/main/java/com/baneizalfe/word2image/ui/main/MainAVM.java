package com.baneizalfe.word2image.ui.main;

import com.baneizalfe.word2image.core.managers.WordManager;
import com.baneizalfe.word2image.ui.base.BaseViewModel;

import javax.inject.Inject;

import timber.log.Timber;

/**
 * Created by baneizalfe on 26.12.17.
 */

public class MainAVM extends BaseViewModel {

    private WordManager mWordManager;

    @Inject
    public MainAVM(WordManager wordManager) {
        mWordManager = wordManager;
    }

    public void submitSearch(CharSequence query) {
        Timber.i("submitSearch " + query);


    }
}
