package com.baneizalfe.word2image.core.network.services;

import com.baneizalfe.word2image.core.model.Word;

import java.util.List;

import io.reactivex.Observable;
import retrofit2.http.GET;
import retrofit2.http.Query;

/**
 * Created by baneizalfe on 26.12.17.
 */

public interface WordService {

    @GET("word")
    Observable<List<Word>> searchWord(@Query("q") String query);

    
}
