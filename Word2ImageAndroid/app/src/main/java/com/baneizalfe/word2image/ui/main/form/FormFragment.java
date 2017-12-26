package com.baneizalfe.word2image.ui.main.form;

import android.arch.lifecycle.ViewModelProvider;
import android.arch.lifecycle.ViewModelProviders;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.text.Editable;
import android.text.TextWatcher;

import com.baneizalfe.word2image.R;
import com.baneizalfe.word2image.databinding.FragmentFormBinding;
import com.baneizalfe.word2image.di.Injectable;
import com.baneizalfe.word2image.ui.base.BaseFragment;
import com.baneizalfe.word2image.ui.main.MainAVM;

import javax.inject.Inject;

/**
 * Created by baneizalfe on 26.12.17.
 */

public class FormFragment extends BaseFragment implements Injectable {

    @Inject
    ViewModelProvider.Factory viewModelFactory;

    private FragmentFormBinding mBinding;

    MainAVM mViewModel;

    @Override
    protected int getLayoutId() {
        return R.layout.fragment_form;
    }

    @Override
    public void onActivityCreated(@Nullable Bundle savedInstanceState) {
        super.onActivityCreated(savedInstanceState);
        mViewModel = ViewModelProviders.of(getActivity(), viewModelFactory).get(MainAVM.class);
        mBinding = FragmentFormBinding.bind(getView());
        mBinding.searchInput.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
                mViewModel.submitSearch(s.toString());
            }
        });
    }
}
