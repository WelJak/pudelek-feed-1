package com.weljak.storageservice.messages;

import com.weljak.storageservice.news.News;
import com.weljak.storageservice.news.NewsRepo;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class DbMessagesService implements MessagesService {
    private final NewsRepo newsRepo;

    @Override
    public List<String> getMessages() {
        List<News> newsList = newsRepo.findAll();
        List<String> response_array = new ArrayList<>();
        for (int i = 0; i < newsList.size(); i++) {
            response_array.add(newsList.get(i).getEntryid());
        }
        return response_array;
    }

}
