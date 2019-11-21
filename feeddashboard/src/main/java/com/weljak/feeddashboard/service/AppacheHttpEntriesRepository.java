package com.weljak.feeddashboard.service;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.reflect.TypeToken;
import com.weljak.feeddashboard.domain.News;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.List;

@Service
public class AppacheHttpEntriesRepository implements EntriesRepository {
    private Gson gson = new Gson();
    @Value("${service.URL}")
    private String BaseURL;
    private CloseableHttpClient client;
    public AppacheHttpEntriesRepository(){
        this.client = HttpClientBuilder.create().build();
    }
    @Override
    public List<News> listAllEntries() {
        try {
            String URL = BaseURL + "messages/all";
            HttpGet request = new HttpGet(URL);
            CloseableHttpResponse response = client.execute(request);
            String result = EntityUtils.toString(response.getEntity());
            JsonArray arr = gson.fromJson(result, JsonObject.class).getAsJsonArray("listOfNews");
            return gson.fromJson(arr, new TypeToken<List<News>>() {
            }.getType());
        } catch (IOException ioe) {
            ioe.printStackTrace();
            return null;
        }
    }

    @Override
    public News getEntryDetails(String id) {
        try{
        String URL = BaseURL + "messages/" + id;
        HttpGet request = new HttpGet(URL);
        CloseableHttpResponse response = client.execute(request);
        String result = EntityUtils.toString(response.getEntity());
        JsonObject obj = gson.fromJson(result, JsonObject.class);
        return gson.fromJson(obj, new TypeToken<News>() {
        }.getType());
        } catch (IOException ioe){
            ioe.printStackTrace();
            return null;
        }
    }
}
