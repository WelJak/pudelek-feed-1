package com.weljak.storageservice.apiclient;

import lombok.Value;

import java.util.List;
@Value
public class MessageToWykop {
    private String uuid;
    private String type;
    private String entryid;
    private String post_date;
    private String title;
    private String description;
    private List<String> tags;
    private String link;
}
