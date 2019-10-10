package com.weljak.storageservice.checker;

import com.weljak.storageservice.news.News;
import com.weljak.storageservice.news.NewsRepo;
import com.weljak.storageservice.news.Tags;
import com.weljak.storageservice.webapi.CheckerRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class DbCheckerService implements CheckerService {
    private final NewsRepo newsRepo;

    @Override
    public boolean checkIfMessageWasSent(CheckerRequest checkerRequest) {
        if (checkerRequest == null) {
            return true;
        }
        final boolean newsExists = newsRepo.existsByEntryid(checkerRequest.getEntryid());
        if (!newsExists) {
            final News news = toNews(checkerRequest);
            newsRepo.save(news);
        }
        return newsExists;
    }

    private Tags convertToTag(String tag) {
        if (tag != null) {
            return Tags.builder().tag(tag).build();
        }
        return null;
    }

    private List<Tags> convertToTagList(List<String> list) {
        if (list != null) {
            return list.stream().map(this::convertToTag).collect(Collectors.toList());
        }
        return new ArrayList<>();
    }

    private News toNews(CheckerRequest checkerRequest) {
        return News.builder()
                .uuid(checkerRequest.getUuid())
                .type(checkerRequest.getType())
                .entryid(checkerRequest.getEntryid())
                .post_date(checkerRequest.getPost_date())
                .title(checkerRequest.getTitle())
                .description(checkerRequest.getDescription())
                .tag(convertToTagList(checkerRequest.getTags()))
                .link(checkerRequest.getLink())
                .wassent(checkerRequest.isWassent())
                .build();
    }

    @Override
    public boolean sendMessage(CheckerRequest checkerRequest) {
        try {
            final News news = toNews(checkerRequest);
            newsRepo.save(news);
            return true;
        } catch (Exception e) {
            System.out.println("something went wrong");
            return false;
        }

    }
}
