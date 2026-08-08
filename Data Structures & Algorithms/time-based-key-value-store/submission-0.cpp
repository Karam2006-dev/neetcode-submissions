class TimeMap {
public:
    map <string, map <int, string>> c;
    TimeMap() {     
    }
    
    void set(string key, string value, int timestamp) {
        c[key][timestamp] = value;
    }
    
    string get(string key, int timestamp) {
        auto it = c[key].upper_bound(timestamp);
        if (it == c[key].begin()) return "";
        --it;
        return it->second;
    }
};