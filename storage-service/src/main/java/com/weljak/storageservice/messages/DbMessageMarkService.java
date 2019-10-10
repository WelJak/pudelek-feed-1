package com.weljak.storageservice.messages;

import com.weljak.storageservice.news.News;
import com.weljak.storageservice.news.NewsRepo;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class DbMessageMarkService implements MessageMarkService {
    private final NewsRepo newsRepo;
    @Override
    public boolean markMessage(String entryid) {
        try {
            final News message = newsRepo.findByEntryid(entryid);
            message.setWassent(true);
            newsRepo.save(message);
            return true;
        }catch (Exception e) {
            System.out.println("something went wrong");
            return false;
        }

    }
}
