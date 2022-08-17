import json
import zoneinfo

from watchman.models import Record

pakistan_timezone = zoneinfo.ZoneInfo('Asia/Karachi')
utc_timezone = zoneinfo.ZoneInfo('UTC')


def change_timezones():
    with open('./cron-settings.json', 'r+') as cron_settings_file:
        cron_settings = json.load(cron_settings_file)
        utc_to_pst = cron_settings['utc_to_pst'] == True

        current_timezone_string = 'UTC' if utc_to_pst else 'PST'
        records = Record.objects.filter(timezone=current_timezone_string)[:3]

        current_timezone = utc_timezone if utc_to_pst else pakistan_timezone
        final_timezone = pakistan_timezone if utc_to_pst else utc_timezone

        for record in records:
            current_datetime = record.recorded_at.replace(
                tzinfo=current_timezone)
            final_datetime = current_datetime.astimezone(final_timezone).replace(
                tzinfo=final_timezone)
            naive_datetime = final_datetime.replace(tzinfo=None)

            record.recorded_at = naive_datetime
            record.timezone = 'PST' if utc_to_pst else 'UTC'
            record.save()

        if Record.objects.filter(timezone=current_timezone_string)[:1].count() == 0:
            cron_settings = json.dumps(
                {"utc_to_pst": not utc_to_pst}, indent=2)
            cron_settings_file.seek(0)
            cron_settings_file.write(cron_settings)
            cron_settings_file.truncate()
