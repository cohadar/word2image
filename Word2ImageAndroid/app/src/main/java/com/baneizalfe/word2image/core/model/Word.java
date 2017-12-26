package com.baneizalfe.word2image.core.model;

import android.os.Parcel;
import android.os.Parcelable;

import com.google.gson.annotations.SerializedName;

import java.util.List;

/**
 * Created by baneizalfe on 26.12.17.
 */

public class Word implements Parcelable {

    @SerializedName("word")
    public String word;

    @SerializedName("weight")
    public int weight;

    @SerializedName("text")
    public String text;

    @SerializedName("imgs")
    public List<String> imgs;


    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(this.word);
        dest.writeInt(this.weight);
        dest.writeString(this.text);
        dest.writeStringList(this.imgs);
    }

    public Word() {
    }

    protected Word(Parcel in) {
        this.word = in.readString();
        this.weight = in.readInt();
        this.text = in.readString();
        this.imgs = in.createStringArrayList();
    }

    public static final Parcelable.Creator<Word> CREATOR = new Parcelable.Creator<Word>() {
        @Override
        public Word createFromParcel(Parcel source) {
            return new Word(source);
        }

        @Override
        public Word[] newArray(int size) {
            return new Word[size];
        }
    };

    @Override
    public boolean equals(Object o) {

        if (o == null) {
            return false;
        }

        if (!(o instanceof Word)) {
            return false;
        }

        if (this.word != null) {
            return this.word.equalsIgnoreCase(((Word) o).word);
        }

        return false;
    }

    @Override
    public int hashCode() {
        int hash = 3;
        hash = 53 * hash + (this.word != null ? this.word.hashCode() : 0);
        return hash;
    }
}
