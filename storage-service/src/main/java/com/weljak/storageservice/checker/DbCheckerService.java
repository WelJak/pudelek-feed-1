package com.weljak.storageservice.checker;

import com.weljak.storageservice.message.News;
import com.weljak.storageservice.message.Tags;
import com.weljak.storageservice.message.newsrepo.NewsRepo;
import com.weljak.storageservice.message.newsrepo.TagsRepo;
import com.weljak.storageservice.webapi.CheckerRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class DbCheckerService implements CheckerService {
    private final NewsRepo newsRepo;
    private final TagsRepo tagsRepo;

    @Override
    public boolean checkIfMessageWasSent(CheckerRequest checkerRequest) {
        if (newsRepo.existsByEntryid(checkerRequest.getEntryid())) {
            return false;
        } else {
            return true;
        }

    }

    public Tags convertToTag(String tag) {
        Tags tags = new Tags();
        tags.setTag(tag);
        return tags;
    }

    public List<Tags> convertToTagList(List<String> list) {
        List<Tags> x = new ArrayList<Tags>();
        for (int i = 0; i < list.size(); i++) {
            x.add(convertToTag(list.get(i)));
        }
        return x;
    }

    public News convertToUuid(String uuid) {
        News news = new News();
        news.setUuid(uuid);
        return news;
    }

    @Override
    public boolean sendMessage(CheckerRequest checkerRequest) {
        try {
            News news = new News();
            news.setEntryid(checkerRequest.getEntryid());
            news.setDescription(checkerRequest.getDescription());
            news.setLink(checkerRequest.getLink());
            news.setPost_date(checkerRequest.getPost_date());
            news.setUuid(checkerRequest.getUuid());
            news.setType(checkerRequest.getType());
            news.setTitle(checkerRequest.getTitle());
            news.setTag(convertToTagList(checkerRequest.getTags()));
            newsRepo.save(news);
            /*for (int a = 0; a < checkerRequest.getTags().size(); a++) {
                Tags tags = new Tags();
                tags.setTag(checkerRequest.getTags().get(a));
                tags.setUuid(convertToUuid(checkerRequest.getUuid()));
                tagsRepo.save(tags);
            }*/

            return true;
        } catch (Exception e) {
            System.out.println("something went wrong");
            return false;
        }

    }
}
