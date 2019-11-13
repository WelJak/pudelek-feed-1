package com.weljak.storageservice.webapi;

import com.weljak.storageservice.news.News;
import lombok.Value;

import java.util.List;

@Value
public class AllMessagesResponse {
    private List<News> listOfNews;
}
