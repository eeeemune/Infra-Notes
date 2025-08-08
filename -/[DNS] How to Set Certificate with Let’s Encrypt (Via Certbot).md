# 💚 How to Set Certificate with Let’s Encrypt (Via Certbot)
## 💛 Install Certbot
```bash
sudo apt update
sudo apt install certbot
```
## 💛 Get Certificate
```bash
sudo certbot certonly --manual --preferred-challenges dns \
  -d "*.coolify.chartmetric.com" \
  -d "coolify.chartmetric.com"
```
## 💛 Add a Record to the Cloudflare
### 🤍 Copy the Content

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/e7a75158-b9c4-4d57-84fa-9858bfaefc38/f9fcb922-bdc5-4707-8686-44f8b95fca67/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NIJOQP%2F20250808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250808T170955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQC4%2BCbx3y0tadjXKXuKJGw0xSrW3nkVB6bjchfTHHx%2FRgIgIgLrqDVCuphS8YscN%2FerQ6bLX0rJL1u%2F9ZFKSz8d2n4qiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNW%2BSVKVd5vNLoN%2FCrcA2i6aVWMKDS8v5lsv%2F97WCSCve%2FcPNyFI%2BaoEm7aPJusb6RT%2ByqFee%2BwK5%2Bk%2BI3M192Kbm6Uc8ii1dhtE%2BwCk2JCEGprJe0D9NPAbEPE2MMUqW5JFREfS%2FPkmE49oipj8VIFUloiH240uqoVhydWQXRMWUxSIRRkwe2uXktEZkqumhCrlGTRC9j8b18x1cC0JuWMamswKTeNxzQiyg5MKDEVQ7qM%2B5c5UGt%2FvWS%2B9eUidH9%2BL9jVXkiz1nXHs7qTR1MVXEL4%2BOVCr%2FWQBpsCMzp5mNZ1rb49l6IXTEdOCwcFmPcnTWoeEKTwTUfB5QmhWb1oiXcJIsXy2FILhhtxDcRTl%2B76NpKMmL1SoWafo9Lkle3F0GaWSCNucqtegZ9KAfJf79Z3sCPLWBaC0UnCwM82rhsAfXjZ2WoA668ODZBa1GFDNaJntAPDC7kydrKBtb2HsovB3ZuNCpDYO3ug6jcI08S8y5t4Ymv03tQeo%2F1YNGkd63M%2BdozWs65p%2BxNcoioPe%2BmTepRJB8OBM67JUxKr52prl3Ul3ClCZwV%2FukRL6%2Fgjm5N3EGO0uZDcS9AP9SbLxJy3efl0qa0b33Vh7AJy4yco2m7M5LXjWRgUrcVRcojeSVRa2rGQEnMnMOSm2MQGOqUB4IPN%2FahyVkwnQfHV0IU7%2BNRl4Y1ej%2F98N4ZpUi4tvEGpqymZjbg2S4oLiuJ%2Fh40cU%2FuNV%2BDzgfC3obW0Q%2B4zWA%2F4JqnmHXUqH1%2BOl48bLKz755KGG9QPvKjzmnkFsgzYjp6GkBoS%2Fg052pHJCqmSEy2ZllPLyPn0jae4Y6xj9k82pnXlLzFZH%2FNo8olhrW6ta%2BIQTluUb2wd%2BbgrjHdleEs5pklY&X-Amz-Signature=279f5bc1441f8101d93ead948e4556cf1cace95145051e9bd6c9f02ca78bf6ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 🤍 Go to Cloudflare Dashboard
- DNS → Records


![](https://prod-files-secure.s3.us-west-2.amazonaws.com/e7a75158-b9c4-4d57-84fa-9858bfaefc38/b373945c-93c7-4329-906e-7809569b0a36/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NIJOQP%2F20250808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250808T170955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQC4%2BCbx3y0tadjXKXuKJGw0xSrW3nkVB6bjchfTHHx%2FRgIgIgLrqDVCuphS8YscN%2FerQ6bLX0rJL1u%2F9ZFKSz8d2n4qiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNW%2BSVKVd5vNLoN%2FCrcA2i6aVWMKDS8v5lsv%2F97WCSCve%2FcPNyFI%2BaoEm7aPJusb6RT%2ByqFee%2BwK5%2Bk%2BI3M192Kbm6Uc8ii1dhtE%2BwCk2JCEGprJe0D9NPAbEPE2MMUqW5JFREfS%2FPkmE49oipj8VIFUloiH240uqoVhydWQXRMWUxSIRRkwe2uXktEZkqumhCrlGTRC9j8b18x1cC0JuWMamswKTeNxzQiyg5MKDEVQ7qM%2B5c5UGt%2FvWS%2B9eUidH9%2BL9jVXkiz1nXHs7qTR1MVXEL4%2BOVCr%2FWQBpsCMzp5mNZ1rb49l6IXTEdOCwcFmPcnTWoeEKTwTUfB5QmhWb1oiXcJIsXy2FILhhtxDcRTl%2B76NpKMmL1SoWafo9Lkle3F0GaWSCNucqtegZ9KAfJf79Z3sCPLWBaC0UnCwM82rhsAfXjZ2WoA668ODZBa1GFDNaJntAPDC7kydrKBtb2HsovB3ZuNCpDYO3ug6jcI08S8y5t4Ymv03tQeo%2F1YNGkd63M%2BdozWs65p%2BxNcoioPe%2BmTepRJB8OBM67JUxKr52prl3Ul3ClCZwV%2FukRL6%2Fgjm5N3EGO0uZDcS9AP9SbLxJy3efl0qa0b33Vh7AJy4yco2m7M5LXjWRgUrcVRcojeSVRa2rGQEnMnMOSm2MQGOqUB4IPN%2FahyVkwnQfHV0IU7%2BNRl4Y1ej%2F98N4ZpUi4tvEGpqymZjbg2S4oLiuJ%2Fh40cU%2FuNV%2BDzgfC3obW0Q%2B4zWA%2F4JqnmHXUqH1%2BOl48bLKz755KGG9QPvKjzmnkFsgzYjp6GkBoS%2Fg052pHJCqmSEy2ZllPLyPn0jae4Y6xj9k82pnXlLzFZH%2FNo8olhrW6ta%2BIQTluUb2wd%2BbgrjHdleEs5pklY&X-Amz-Signature=595e42b4abbacddfbd8d118626175f7bc042814df84409f4a2ee5fe15ee44fe2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 🤍 Add The Record
****

> - Type: TXT
> 
> - Name: _acme-challenge.coolify
> 
> - Content: [the long string certbot gave you]
> 
## 💛 (Optional) Configure Traefik to Use the Certificate
### 🤍 Set the Certificate Key to Proper Path

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/e7a75158-b9c4-4d57-84fa-9858bfaefc38/0d0696d6-5fa8-47b7-84e2-c77bc3192e7f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4NIJOQP%2F20250808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250808T170955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQC4%2BCbx3y0tadjXKXuKJGw0xSrW3nkVB6bjchfTHHx%2FRgIgIgLrqDVCuphS8YscN%2FerQ6bLX0rJL1u%2F9ZFKSz8d2n4qiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNW%2BSVKVd5vNLoN%2FCrcA2i6aVWMKDS8v5lsv%2F97WCSCve%2FcPNyFI%2BaoEm7aPJusb6RT%2ByqFee%2BwK5%2Bk%2BI3M192Kbm6Uc8ii1dhtE%2BwCk2JCEGprJe0D9NPAbEPE2MMUqW5JFREfS%2FPkmE49oipj8VIFUloiH240uqoVhydWQXRMWUxSIRRkwe2uXktEZkqumhCrlGTRC9j8b18x1cC0JuWMamswKTeNxzQiyg5MKDEVQ7qM%2B5c5UGt%2FvWS%2B9eUidH9%2BL9jVXkiz1nXHs7qTR1MVXEL4%2BOVCr%2FWQBpsCMzp5mNZ1rb49l6IXTEdOCwcFmPcnTWoeEKTwTUfB5QmhWb1oiXcJIsXy2FILhhtxDcRTl%2B76NpKMmL1SoWafo9Lkle3F0GaWSCNucqtegZ9KAfJf79Z3sCPLWBaC0UnCwM82rhsAfXjZ2WoA668ODZBa1GFDNaJntAPDC7kydrKBtb2HsovB3ZuNCpDYO3ug6jcI08S8y5t4Ymv03tQeo%2F1YNGkd63M%2BdozWs65p%2BxNcoioPe%2BmTepRJB8OBM67JUxKr52prl3Ul3ClCZwV%2FukRL6%2Fgjm5N3EGO0uZDcS9AP9SbLxJy3efl0qa0b33Vh7AJy4yco2m7M5LXjWRgUrcVRcojeSVRa2rGQEnMnMOSm2MQGOqUB4IPN%2FahyVkwnQfHV0IU7%2BNRl4Y1ej%2F98N4ZpUi4tvEGpqymZjbg2S4oLiuJ%2Fh40cU%2FuNV%2BDzgfC3obW0Q%2B4zWA%2F4JqnmHXUqH1%2BOl48bLKz755KGG9QPvKjzmnkFsgzYjp6GkBoS%2Fg052pHJCqmSEy2ZllPLyPn0jae4Y6xj9k82pnXlLzFZH%2FNo8olhrW6ta%2BIQTluUb2wd%2BbgrjHdleEs5pklY&X-Amz-Signature=f29e2662098e27f0cb945e86d65e7a3a2c14a49dd6bfe120fa036ff1c9e776e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```bash
sudo cp /etc/letsencrypt/live/coolify.chartmetric.com/fullchain.pem /data/coolify/proxy/certs/chartmetric.com.cert
sudo cp /etc/letsencrypt/live/coolify.chartmetric.com/privkey.pem /data/coolify/proxy/certs/chartmetric.com.key
```
### 🤍 (Optional) Check the content looks correct
```bash
sudo openssl x509 -in /data/coolify/proxy/coolify.chartmetric.com.crt -text -noout | head -20
```
### 🤍 Configure Traefik to Use the Certificate
```yaml
# certificate.yml
tls:
  certificates:
    -
      certFile: /traefik/certs/chartmetric.com.cert
      keyFile: /traefik/certs/chartmetric.com.key
```
