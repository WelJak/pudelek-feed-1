package com.weljak.storageservice.messages;

import com.weljak.storageservice.news.News;

import java.util.List;

public interface MessagesService {
    public List<String> getMessages();

    public boolean markMessage(String entryid);

    public News getMessage(String entryid);
}
