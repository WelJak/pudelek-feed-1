package com.weljak.storageservice.checker;

import com.weljak.storageservice.message.newsrepo.NewsRepo;
import com.weljak.storageservice.webapi.CheckerRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class DbCheckerService implements CheckerService {
    private final NewsRepo newsRepo;

    @Override
    public boolean checkIfMessageWasSent(CheckerRequest checkerRequest) {
        if (newsRepo.existsByEntryid(checkerRequest.getEntryid())){
            return true;
        }else {
            return false;
        }
    }
}
