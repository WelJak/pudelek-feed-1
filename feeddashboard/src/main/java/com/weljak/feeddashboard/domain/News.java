package com.weljak.feeddashboard.domain;

import lombok.Value;

import java.util.List;

@Value
public class News {
    private String uuid;
    private String type;
    private String entryid;
    private String post_date;
    private String title;
    private String description;
    private List<Tags> tags;
    private String link;
    private boolean wassent;
}
