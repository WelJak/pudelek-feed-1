package com.weljak.storageservice.webapi;

import lombok.Value;

import java.util.List;

@Value
public class CheckerRequest {
    private String id;
    private String date;
    private String title;
    private String description;
    private List<String> tags;
    private String link;

}
