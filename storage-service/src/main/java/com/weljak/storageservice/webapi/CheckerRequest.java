package com.weljak.storageservice.webapi;

import lombok.Data;

import java.util.Arrays;

@Data
public class CheckerRequest {
    private String id;
    private String date;
    private String title;
    private String description;
    private String[] tags;
    private String link;
    private String[] array;

    public void getmessage() {
        this.setId("message id");
        this.setDate("message date");
        this.setTitle("message title");
        this.setDescription("message desc");
        this.setTags(new String[]{"tag1", "tag2"});
        this.setLink("message link");
    }

    public void createArray(){
        this.array = new String[]{this.id, this.date, this.title, this.description, Arrays.toString(this.tags), this.link};
    }

}
