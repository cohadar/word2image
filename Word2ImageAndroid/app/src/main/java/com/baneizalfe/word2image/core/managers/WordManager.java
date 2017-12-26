package com.baneizalfe.word2image.core.managers;

import com.baneizalfe.word2image.core.model.Word;
import com.baneizalfe.word2image.core.network.services.WordService;

import io.reactivex.Observable;

/**
 * Created by baneizalfe on 26.12.17.
 */

public class WordManager {

    private WordService mWordService;

    public WordManager(WordService wordService) {
        mWordService = wordService;
    }

}
