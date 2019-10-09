package com.weljak.storageservice.webapi;

import com.weljak.storageservice.news.Tags;
import lombok.Value;

import java.util.List;

@Value
public class MessageDetailResponse {
    private String uuid;
    private String type;
    private String entryid;
    private String post_date;
    private String title;
    private String description;
    private List<Tags> tags;
    private String link;
}
