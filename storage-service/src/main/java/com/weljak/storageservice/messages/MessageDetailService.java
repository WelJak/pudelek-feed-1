package com.weljak.storageservice.messages;

import com.weljak.storageservice.news.News;

public interface MessageDetailService {
    public News getMessage(String entryid);
}
