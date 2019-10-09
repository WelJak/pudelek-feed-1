package com.weljak.storageservice.messages;

import com.weljak.storageservice.news.News;
import com.weljak.storageservice.news.NewsRepo;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class DbMessageDetailService implements MessageDetailService {
    private final NewsRepo newsRepo;

    @Override
    public News getMessage(String entryid) {
        final News message = newsRepo.findByEntryid(entryid);
        return message;
    }
}
