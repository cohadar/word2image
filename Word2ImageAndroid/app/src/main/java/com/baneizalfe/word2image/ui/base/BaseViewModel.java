package com.baneizalfe.word2image.ui.base;

import android.arch.lifecycle.LiveData;
import android.arch.lifecycle.MutableLiveData;
import android.arch.lifecycle.ViewModel;

import java.io.IOException;

import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.disposables.Disposable;
import retrofit2.HttpException;

/**
 * Created by baneizalfe on 26.12.17.
 */

public class BaseViewModel extends ViewModel {

    private final CompositeDisposable mCompositeDisposable = new CompositeDisposable();

    protected void subscribe(Disposable d) {
        mCompositeDisposable.add(d);
    }

    protected MutableLiveData<Boolean> mShowLoading = new MutableLiveData<>();
    protected MutableLiveData<Boolean> mShowNetworkError = new MutableLiveData<>();
    protected MutableLiveData<String> mShowError = new MutableLiveData<>();

    public BaseViewModel() {
        mShowLoading.setValue(true);
        mShowNetworkError.setValue(false);
        mShowError.setValue(null);
    }

    @Override
    protected void onCleared() {
        mCompositeDisposable.clear();
        super.onCleared();
    }

    public LiveData<Boolean> outShowLoading() {
        return mShowLoading;
    }

    public LiveData<Boolean> outShowNetworkError() {
        return mShowNetworkError;
    }

    public LiveData<String> outShowError() {
        return mShowError;
    }

    protected void handleError(Throwable e) {
        if (e instanceof HttpException) {
            HttpException exception = (HttpException) e;
            if (exception.code() == 401) {
                handleUnauthorizedError();
            } else {
                handleError();
            }

        } else if (e instanceof IOException) {
            handleNetworkError();
        } else {
            handleError();
        }
    }

    protected void handleUnauthorizedError() {
        mShowError.setValue("You have been logged out");
    }

    protected void handleNetworkError() {
        mShowNetworkError.setValue(true);
    }

    protected void handleError() {
        mShowError.setValue("An error occurred");
    }
}
