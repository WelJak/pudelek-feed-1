package com.weljak.storageservice.messages;

import com.weljak.storageservice.news.News;
import com.weljak.storageservice.news.NewsRepo;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Slf4j
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

    @Override
    public boolean markMessage(String entryid) {
        try {
            final News message = newsRepo.findByEntryid(entryid);
            message.setWassent(true);
            newsRepo.save(message);
            return true;
        } catch (Exception e) {
            log.info("an error occurred during process: ");
            e.printStackTrace();
            return false;
        }
    }

    @Override
    public News getMessage(String entryid) {
        final News message = newsRepo.findByEntryid(entryid);
        return message;
    }

}
