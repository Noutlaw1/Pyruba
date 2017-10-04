# Pyruba
Library for accessing and working with the Aruba Activate api

## Summary

I am involved in a large Aruba Remote Access deployment and since I hate doing things efficiently, I wanted to script parts of our deployment process. Activate has an API, though as far as I can see, it does not seem to play nice with Python's basic JSON library. Additionally, the Activate web application itself has no way I have found of mass provisioning access points, which is a real painful point when you have thousands of these things to roll out. I am also using it as a learning opportunity to try and do things the best way rather than hacking them together.

This is (as you can tell) in its very early stages but if you get some use from it, I'd love to know. Feel free to use it and change it as you please.

### Reference

After you import it, create an object to get started.

```
Sample_Aruba_Object = Aruba(username, password)

#Then connect. I think I might make instantiating the object connect as well but I will figure that out later.
Sample_Aruba_Object.Connect()

#You can search your RAP inventory like this. Right now you can search by one parameter: RAP Name, MAC address, or serial number. It returns a JSON object.
RAPS = Sample_Aruba_Object.SearchInventory(name="RAP-1")

#You can also provision the RAPs in Activate. It takes the attributes you want to assign to it in Activate as parameters, such as RAP Name or the associated user's name. The MAC address is required in order to find the right AP which uses colons. Don't use the folder-group parameter for now. Going to find a way to translate from the long ID it has in activate to something user friendly.
Sample_Aruba_Object.ProvisionRAP("00:14:22:01:23:45", rap_user_name="sample_user", rap_name="sample_RAP_name")
```

### Future ideas

One of the main things I want to do is a feature that will take a CSV and change RAP attributes in bulk. I'd also like to put some sort of GUI or front-end on it as to make it simpler to use (also more stylish!)


