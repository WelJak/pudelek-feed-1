package com.weljak.storageservice.apiclient;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;


public class WykopService implements WykopApiService {
    private String WYKOP_LOGIN_URL = "https://a2.wykop.pl/Login/Index/";
    private String WYKOP_GET_HOT_URL = "https://a2.wykop.pl/Hits/Popular/";
    private String WYKOP_LINK_DRAFT_URL = "https://a2.wykop.pl/Addlink/Draft/";
    private String WYKOP_PREPARE_THUMBNAIL_URL = "https://a2.wykop.pl/Addlink/Images/";
    private String WYKOP_ADD_LINK_URL = "https://a2.wykop.pl/Addlink/Add/";
    private String CURRENT_APP_DIR = System.getProperty("user.dir");
    private String USERKEY_FILE_DIR = CURRENT_APP_DIR + "/src/main/java/com/weljak/storageservice/apiclient/userkey";
    private String APPKEY;
    private String WYKOP_ACC_KEY;
    private String WYKOP_LOGIN;
    private String WYKOP_SECRET;
    private CloseableHttpClient client;
    private Gson gson = new Gson();
    private String USERKEY;

    public WykopService(String appkey, String acc_key, String login, String secret) {
        this.APPKEY = appkey;
        this.WYKOP_ACC_KEY = acc_key;
        this.WYKOP_LOGIN = login;
        this.WYKOP_SECRET = secret;
        this.client = HttpClientBuilder.create().build();

    }

    public LoginResponse login() {
        try {
            HttpPost post = createPost(WYKOP_LOGIN_URL + "appkey/" + APPKEY + "/accountkey/" + WYKOP_ACC_KEY,
                    WYKOP_LOGIN + "," + WYKOP_ACC_KEY);
            List<NameValuePair> urlPostParams = new ArrayList<>();
            urlPostParams.add(new BasicNameValuePair("login", WYKOP_LOGIN));
            urlPostParams.add(new BasicNameValuePair("accountkey", WYKOP_ACC_KEY));
            post.setEntity(new UrlEncodedFormEntity(urlPostParams));
            CloseableHttpResponse response = client.execute(post);
            String result = EntityUtils.toString(response.getEntity());
            JsonObject jsonResponse = gson.fromJson(result, JsonObject.class);
            JsonElement jsonUserkey = jsonResponse.getAsJsonObject("data").getAsJsonPrimitive("userkey");
            String userkey = jsonUserkey.toString();
            LoginResponse loginResponse = new LoginResponse(userkey.substring(1, userkey.length() - 2));
            writeUserKeyToFile(loginResponse.getUserkey());
            return loginResponse;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public PrepareLinkResponse prepareLinkForPosting(MessageToWykop message) {
        try {
            this.USERKEY = readUserKeyFromFile();
            HttpPost post = createPost(WYKOP_LINK_DRAFT_URL + "appkey/" + APPKEY + "/userkey/" + "dsSRT:4YoSI:1d4Dc:5je4v:bjAQX:3K3v", message.getLink());
            List<NameValuePair> urlPostParams = new ArrayList<>();
            urlPostParams.add(new BasicNameValuePair("url", message.getLink()));
            post.setEntity(new UrlEncodedFormEntity(urlPostParams));
            CloseableHttpResponse response = client.execute(post);
            String result = EntityUtils.toString(response.getEntity());
            JsonObject jsonResponse = gson.fromJson(result, JsonObject.class);
            JsonElement jsonLinkKey = jsonResponse.getAsJsonObject("data").getAsJsonPrimitive("key");
            PrepareLinkResponse prepareLinkResponse = new PrepareLinkResponse(jsonLinkKey.toString().substring(1, jsonLinkKey.toString().length() - 1));
            return prepareLinkResponse;
        } catch (IOException ioe) {
            ioe.printStackTrace();
            return null;
        }
    }

    public PreparePhotoResponse prepareNewsThumbnail(PrepareLinkResponse prepareLinkResponse) {
        this.USERKEY = readUserKeyFromFile();
        try {
            HttpGet get = createGetRequest(WYKOP_PREPARE_THUMBNAIL_URL + "key/" + prepareLinkResponse.getKey() + "/appkey/" + APPKEY + "/userkey/" + USERKEY);
            CloseableHttpResponse response = client.execute(get);
            String result = EntityUtils.toString(response.getEntity());
            JsonObject jsonResponse = gson.fromJson(result, JsonObject.class);
            JsonArray jsonPhotoKey = jsonResponse.getAsJsonArray("data");
            String arrayElement = jsonPhotoKey.get(0).toString();
            JsonObject jsonElement = gson.fromJson(arrayElement, JsonObject.class);
            JsonElement jsonLinkKey = jsonElement.getAsJsonPrimitive("key");
            PreparePhotoResponse preparePhotoResponse = new PreparePhotoResponse(jsonLinkKey.toString().substring(1, jsonLinkKey.toString().length() - 1));
            return preparePhotoResponse;
        } catch (IOException ioe) {
            ioe.printStackTrace();
            return null;
        }
    }

    public String addLinkOnWykop(PrepareLinkResponse prepareLinkResponse, PreparePhotoResponse preparePhotoResponse, MessageToWykop message) {
        /*try{
            String postparams;
            HttpPost post = createPost(WYKOP_ADD_LINK_URL+"key/" + prepareLinkResponse.getKey()+"/appkey/"+ APPKEY + "/userkey/"+USERKEY,postparams);
            return null;
        }catch (IOException ioe) {
            ioe.printStackTrace();
            return null;
        }*/
        return null;
    }


    public String getHits() {
        try {
            String url = WYKOP_GET_HOT_URL + "appkey/" + APPKEY;
            String checksum = createMd5Checksum(WYKOP_SECRET, url, "");
            HttpGet request = new HttpGet(url);
            request.addHeader("apisign", checksum);
            request.addHeader("Content-type", "application/x-www-form-urlencoded");
            CloseableHttpResponse response = client.execute(request);
            String result = EntityUtils.toString(response.getEntity(), "UTF-8");
            return result;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static String createMd5Checksum(String secret, String url, String postparams) {
        String valueToCount = secret + url + postparams;
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(valueToCount.getBytes());
            BigInteger no = new BigInteger(1, messageDigest);
            String hash = no.toString(16);
            while (hash.length() < 32) {
                hash = "0" + hash;
            }
            return hash;
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
    }

    private HttpPost createPost(String url, String postparams) {
        HttpPost post = new HttpPost(url);
        String checksum = createMd5Checksum(WYKOP_SECRET, url, postparams);
        post.addHeader("apisign", checksum);
        post.addHeader("Content-type", "application/x-www-form-urlencoded");
        return post;
    }

    private HttpGet createGetRequest(String url) {
        HttpGet get = new HttpGet(url);
        String checksum = createMd5Checksum(WYKOP_SECRET, url, "");
        get.addHeader("apisign", checksum);
        get.addHeader("Content-type", "application/x-www-form-urlencoded");
        return get;
    }

    private void writeUserKeyToFile(String userkey) {
        try {
            Files.write(Paths.get(USERKEY_FILE_DIR), userkey.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private String readUserKeyFromFile() {
        try (Stream<String> userkey = Files.lines(Paths.get(USERKEY_FILE_DIR))) {
            return userkey
                    .findFirst()
                    .get();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

}
