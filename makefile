CRLS=gds5-16.crl CloudflareIncECCCA-3.crl GTS1O1core.crl gsr2.crl root-r2.crl \
		 sca1b.crl
CSVS=$(subst .crl,.csv,$(CRLS))

.PHONY:all
all: csvs

# Downloads all crls
.PHONY:crls
crls: $(CRLS)

gds5-16.crl:
	wget http://crl.godaddy.com/gds5-16.crl

CloudflareIncECCCA-3.crl:
	wget http://crl4.digicert.com/CloudflareIncECCCA-3.crl

GTS1O1core.crl:
	wget http://crl.pki.goog/GTS1O1core.crl

gsr2.crl:
	wget http://crl.pki.goog/gsr2/gsr2.crl

root-r2.crl:
	wget http://crl.globalsign.net/root-r2.crl

sca1b.crl:
	wget http://crl.sca1b.amazontrust.com/sca1b.crl

.PHONY:csvs
csvs: $(CSVS)

%.csv: %.crl parse-crl.py
	./parse-crl.py -i $< > $@

# Removes all generated files
.PHONY:clean
clean:
	rm $(CRLS) $(CSVS)
