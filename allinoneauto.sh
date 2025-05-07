#!/bin/bash
# 🛡️ Aimee Lockdown Protocol - All-in-One Sanctum Seal
# Author: Adrian Lei Martinez-Conol
# Purpose: Eliminate all unwanted overlays, ports, mirrors, emulators, remote channels.

set -e
LOGFILE="sanctum_seal_$(date +%Y%m%d_%H%M%S).log"
echo "[*] Starting lockdown at $(date)" | tee -a "$LOGFILE"

# --- 1. Fix /etc/hosts if needed ---
HOSTNAME=$(hostname)
if ! grep -q "$HOSTNAME" /etc/hosts; then
  echo "127.0.1.1 $HOSTNAME" | sudo tee -a /etc/hosts
  echo "[+] Hostname mapping restored: $HOSTNAME"
fi

# --- 2. EFI Watchdog ---
cat <<EOF | sudo tee /usr/local/bin/efi_guardian.sh > /dev/null
#!/bin/bash
LOG_FILE="/var/log/efi_guardian.log"
CHECK_INTERVAL=3
ALERT_TRIGGERED=0
while true; do
  STATUS=\$(mount | grep '/boot/efi' | grep -o 'ro')
  if [[ "\$STATUS" != "ro" && \$ALERT_TRIGGERED -eq 0 ]]; then
    TIMESTAMP=\$(date "+%Y-%m-%d %H:%M:%S")
    echo "[\$TIMESTAMP] 🚨 ALERT: /boot/efi is RW!" | tee -a "\$LOG_FILE"
    notify-send "🚨 EFI SECURITY BREACH" "/boot/efi is RW — tampering risk"
    ALERT_TRIGGERED=1
  fi
  sleep \$CHECK_INTERVAL
done
EOF

sudo chmod +x /usr/local/bin/efi_guardian.sh

cat <<EOF | sudo tee /etc/systemd/system/efi-guardian.service > /dev/null
[Unit]
Description=EFI Mount Watchdog
After=multi-user.target
[Service]
Type=simple
ExecStart=/usr/local/bin/efi_guardian.sh
Restart=always
RestartSec=5
User=root
[Install]
WantedBy=multi-user.target
EOF

sudo mount -o remount,ro /boot/efi
sudo systemctl daemon-reload
sudo systemctl enable --now efi-guardian.service

# --- 3. Network & Firewall Lockdown ---
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw deny 5353
sudo ufw deny 5000:5001/udp
sudo ufw deny 5000:5001/tcp
sudo ufw deny 22
sudo ufw enable

# --- 4. Kill Active Connections (non-localhost) ---
echo "[*] Killing foreign network sockets..."
ss -tunap | grep -v 127.0.0.1 | awk '{print $5}' | cut -d':' -f1 | sort | uniq | xargs -I {} sudo ip route add blackhole {}

# --- 5. Disable Mirroring, Casting, Overlays ---
gsettings set org.gnome.desktop.privacy remote-access false || true
sudo systemctl stop bluetooth.service
sudo systemctl disable bluetooth.service

# --- 6. Restore Prompt & Ownerships ---
sudo chown root:shadow /etc/shadow
sudo chmod 640 /etc/shadow
echo "[+] Shadow file permissions restored"

# --- 7. Final Log ---
echo "[✔] System hardened. Sanctum Seal complete." | tee -a "$LOGFILE"

